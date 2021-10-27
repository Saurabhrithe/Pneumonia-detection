<script>
        const inpFile = document.getElementById("pwd");
        const previewContainer = document.getElementById("img-preview");
        const previewImage = previewContainer.querySelector(".img-preview-img");
        const previewImgDefault = previewContainer.querySelector(".img-preview__default-text");

        inpFile.addEventListener("change", function(){
            const file = this.files[0];
            if (file){
                const reader = new FileReader();

                previewImgDefault.style.display = "none";
                previewImage.style.display = "block";

                reader.addEventListener("load", function(){
                    console.log(this);
                    previewImage.setAttribute("src", this.result);
                });
                reader.readAsDataURL(file);
            }
        });
    </script>
