from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import JsonResponse

from .models import Product, Category, Comment
from .forms import ProductForm, CommentForm

# Create your views here.


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = product.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.product = product
                new_comment.author = request.user
                new_comment.save()
                # Approval notice
                messages.info(request, "Your comment is awaiting approval")
                return redirect('product_detail', product_id=product_id)
            else:
                messages.error(
                    request, "Error submitting comment - please check the form")
        else:
            messages.error(
                request, "You must be logged in to leave a comment.")
            return redirect('home')  # Redirect to login page if not logged in
    else:
        comment_form = CommentForm()

    context = {
        "product": product,
        "comments": comments,
        "comment_form": comment_form,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def comment_edit(request, product_id, comment_id):
    product = get_object_or_404(Product, pk=product_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            updated_comment = comment_form.save(commit=False)
            updated_comment.product = product
            updated_comment.active = False  # Reset approval status after edit
            updated_comment.save()
            messages.success(request, "Comment updated successfully!")
            return redirect(reverse("product_detail", args=[product.id]))
    else:
        comment_form = CommentForm(instance=comment)

    context = {
        "product": product,
        "comment_form": comment_form,
        "editing_comment_id": comment_id,
    }
    return render(request, "products/comment_edit.html", context)

@login_required
def comment_delete(request, product_id, comment_id):
    """
    Delete a product comment
    """
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment.author == request.user or request.user.is_superuser:
            comment.delete()
            messages.success(request, "Comment deleted successfully")
            # Return JSON if this is an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"success": True})
        return redirect(reverse("product_detail", args=[product.id]))
    messages.error(request, "Error deleting comment")
    return redirect(reverse("product_detail", args=[product.id]))