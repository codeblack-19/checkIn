<template>
    <div class="banner">
        <div class="text-slide">
            <div class="px-10"> 
                <h2 class="text-xl-h1 text-lg-h2 font-weight-bold mb-10">
                    ...never get bored <br />
                    on <span>checkIn</span>...
                </h2>
                <p class="text-h7 text-blue-grey-lighten-1 text-left">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis possimus hic deserunt incidunt rem dolorum amet
                    aspernatur cupiditate facilis quae doloribus labore fugiat, repellendus nemo perferendis odio, consequuntur iusto
                    porro.
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style>
.banner {
    height: 100vh;
    z-index: 0;
    position: relative;
}

.banner::before {
    content: "";
    position: absolute;
    z-index: -1;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url(../../assets/images/toa-heftiba-atMZab62f0g-unsplash.jpg) 39% 19%;
    -webkit-clip-path: polygon(52% 0, 100% 0%, 100% 100%, 100% 1000%, 40% 1000%, 40% 100%);
    clip-path: polygon(52% 0, 100% 0%, 100% 100%, 100% 1000%, 40% 1000%, 40% 100%);
}

.text-slide {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: left;
}

.text-slide p{
    width: 37%;
}
</style>