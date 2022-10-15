<template>
      <!-- header -->
      <NavBar />

      <!-- panels -->
      <v-row no-gutters class="panel-bx">
        <!-- left panel -->
        <LeftPanel />

        <!-- right panel -->
        <RightPanel />
      </v-row>
</template>

<script setup>
import NavBar from '../components/NavBar.vue';
import LeftPanel from '../components/HomeComps/LeftPanel.vue';
import RightPanel from '../components/HomeComps/RightPanel.vue';

</script>

<style>
.panel-bx{
  height: calc(100vh - 6em);
}

@media (max-width: 768px) {
  .panel-bx {
    height: calc(100vh - 5em);
  }
}

@media (max-width: 375px) {
  .panel-bx {
    height: calc(100vh - 4.7em);
  }
}

.panel{
  position: relative;
  height: 100%;
}
</style>