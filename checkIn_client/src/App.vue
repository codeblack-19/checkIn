<template>
  <v-app>
    <v-main>
      <div class="chat-body">
        <div class="cht-bx rounded-sm">
          <router-view />
        </div>
      </div>
    </v-main>
  </v-app>
</template>

<script setup>

</script>

<style>
html {
  overflow: hidden !important;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

html::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.chat-body {
  padding: 1%;
  height: 100vh;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.811)),
    url(./assets/images/nicolas-houdayer-KdCjVKIX4gk-unsplash.jpg);
  background-position: center;
  background-size: cover;
}
</style>