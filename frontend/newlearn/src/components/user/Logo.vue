<template>
    <span class=" d-flex flex-column " style="width:180px;">
        <span>
            <img src="../../assets/images/Logo.png">
        </span>
        <!-- <h5 class="mt-2 mb-5" style="color:#464545">
            NEW LEARN
        </h5>  -->
    </span>
    
</template>

<script>
import LogoImage from "../../assets/images/Logo.png";
export default {
    name: "Logo",
    data: () => {
        return { LogoImage };
    }
}
</script>

<style scoped>
    img{
        cursor: pointer;
        height:50px;
        background-color:#350303;
    }
</style>