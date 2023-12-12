var modal = document.getElementById("modal");
    var modalImg = document.getElementById("modal-img");
    function showImage(src) {
        modal.classList.remove('invisible');
        modalImg.src = src;
    }
    function closeImage() {
        modal.classList.add('invisible');
    }