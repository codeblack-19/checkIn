<template>
    <v-toolbar dense class="glass-toolbar mb-1">

        <v-app-bar-nav-icon color="grey-lighten-4" class="d-md-none"  @click="drawerOpen = !drawerOpen"></v-app-bar-nav-icon>

        <v-toolbar-title class="text-h5 font-weight-bold text-grey-lighten-4">
            checkIn
        </v-toolbar-title>
    
        <v-spacer></v-spacer>
    
        <v-chip class="mx-4 pa-1" color="grey-lighten-5" text-color="lime-darken-3">
            <v-avatar  left>
                <v-icon color="grey-lighten-4">mdi-account-circle</v-icon>
            </v-avatar>
            <span class="d-none d-md-flex ma-1">
                danny Sunday
            </span>
        </v-chip>
    </v-toolbar>
    <v-navigation-drawer v-model="drawerOpen" absolute temporary>
        <div class="pa-4">
            <v-toolbar-title class="text-h5 font-weight-bold text-teal-darken-1">
                checkIn
            </v-toolbar-title>
        </div>
    
        <v-divider></v-divider>
    
        
    </v-navigation-drawer>
</template>

<script setup>
import { ref } from 'vue';

const innerWidth = window.innerWidth
const drawerOpen = ref(false)

</script>

<style>
.glass-toolbar{
    background-color: rgba(255, 255, 255, 0.312) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    backdrop-filter: blur(4px) !important;
}
</style>