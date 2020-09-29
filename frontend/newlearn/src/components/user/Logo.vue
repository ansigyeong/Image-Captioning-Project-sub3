<template>
    <div class=" d-flex flex-column align-items-center">
       
        <div>
            <img src="../../assets/images/LogoImage.png">
        </div>
        <h5 class="mt-2 mb-5" style="color:#464545">
            NEW LEARN
        </h5>
        
    </div>
    
</template>

<script>
import LogoImage from "../../assets/images/LogoImage.png";
export default {
    name: "Logo",
    data: () => {
        return { LogoImage };
    }
}
</script>