document.addEventListener("DOMContentLoaded", function() {    
    // Get elements
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    // Edit functionality
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            const commentId = e.target.getAttribute("comment_id");
            const commentContent = document.getElementById(`comment${commentId}`).querySelector('div').innerText.trim();
            commentText.value = commentContent;
            const editUrl = e.target.getAttribute("data-edit-url");
            commentForm.setAttribute("action", editUrl);
            submitButton.innerText = "Update";
            commentForm.scrollIntoView({ behavior: "smooth" });
        });
    }

    // Delete functionality
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment-id");
            deleteConfirm.setAttribute("data-comment-id", commentId);
            deleteModal.show();
        });
    }

    deleteConfirm.addEventListener("click", function(e) {
        e.preventDefault();
        const commentId = this.getAttribute("data-comment-id");
        const productId = document.querySelector('.btn-delete[data-comment-id="' + commentId + '"]').getAttribute("data-product");
        const deleteUrl = `/comment/delete/${productId}/${commentId}/`;

        fetch(deleteUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            }
        }).then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        }).then(data => {
            if (data.success) {
                location.reload(); // Reload page if deletion was successful
            } else {
                alert('Error deleting comment: ' + data.message);
            }
        }).catch(error => {
            console.error('Error:', error);
            alert('An error occurred while deleting the comment');
        });
    });


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };
});
