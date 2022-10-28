<template>
    <v-toolbar dense class="glass-toolbar mb-1">

        <v-app-bar-nav-icon color="grey-lighten-4" class="d-md-none"  @click="drawerOpen = !drawerOpen"></v-app-bar-nav-icon>

        <v-toolbar-title class="text-h5 font-weight-bold text-grey-lighten-4">
            checkIn
        </v-toolbar-title>
    
        <v-spacer></v-spacer>
        
        <v-menu transition="scale-transition" location="top" >
            <template v-slot:activator="{ props }">
                <v-chip class="mx-4 pa-1" color="grey-lighten-5" text-color="lime-darken-3" dark v-bind="props">
                    <v-avatar left>
                        <v-icon color="grey-lighten-4">mdi-account-circle</v-icon>
                    </v-avatar>
                    <span class="d-none d-md-flex ma-1">
                        danny Sunday
                    </span>
                </v-chip>
            </template>
            <v-card class="py-3 mt-2 bg-grey-darken-2" min-width="190px">
                <div class="mx-auto text-center">
                    <v-avatar color="grey-darken-3" size="38">
                        <v-icon color="grey-lighten-4">mdi-account-circle</v-icon>
                    </v-avatar>
                    <h3 class="text-subtitle-1">danny sunday</h3>
                    <v-btn rounded-sm text class="bg-grey-lighten-3" size="small">
                        Edit Profile
                    </v-btn>
                    <v-divider class="my-3"></v-divider>
                    <v-btn rounded-sm text class="bg-grey-lighten-3" size="small">
                        Create Group
                    </v-btn>
                    <v-divider class="my-3"></v-divider>
                    <v-btn rounded-sm @click="logout" text class="bg-grey-lighten-3" size="small">
                        Logout
                    </v-btn>
                </div>
            </v-card>
        </v-menu>
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
import {useRouter} from 'vue-router';

const drawerOpen = ref(false)
const router = useRouter()

const logout = () => {
    return router.replace({path: '/login'})
}
</script>

<style>
.glass-toolbar{
    background-color: rgba(255, 255, 255, 0.312) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    backdrop-filter: blur(4px) !important;
}
</style>