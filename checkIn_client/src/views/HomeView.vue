<template>
  <div class="chat-body">
    <div class="cht-bx rounded-sm">
      <!-- header -->
      <NavBar />

      <!-- panels -->
      <v-row no-gutters class="panel-bx">
        <!-- left panel -->
        <LeftPanel />

        <!-- right panel -->
        <RightPanel />
      </v-row>
    </div>
  </div>
</template>

<script setup>
import NavBar from '../components/NavBar.vue';
import LeftPanel from '../components/HomeComps/LeftPanel.vue';
import RightPanel from '../components/HomeComps/RightPanel.vue';

</script>

<style>
.chat-body {
  padding: 2%;
  height: 100vh;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.811)),
    url(../assets/images/nicolas-houdayer-KdCjVKIX4gk-unsplash.jpg);
  background-position: center;
  background-size: cover;
}

.panel-bx{
  height: calc(100vh - 130px);
}

.panel{
  position: relative;
  height: 100%;
}
</style>