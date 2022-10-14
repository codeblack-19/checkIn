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
  height: calc(100vh - 95px);
}

.panel{
  position: relative;
  height: 100%;
}
</style>