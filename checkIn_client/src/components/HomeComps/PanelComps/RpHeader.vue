<template>
    <div class="gp_info_bx px-3 py-2 d-flex">
        <v-menu transition="scale-transition" >
            <template v-slot:activator="{ props }">
                <v-btn icon size="42" class="bg-grey-darken-1 mr-2" dark v-bind="props">
                    <v-icon dark>
                        mdi-account-multiple
                    </v-icon>
                </v-btn>
            </template>
        
            <v-list>
                <v-list-item v-for="n in 4" :key="n">
                    <v-list-item-title>tab - {{ n }}</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
        <div class="d-flex flex-column">
            <div class="d-flex">
                <p class="text-subtitle-2 text-grey-lighten-4">
                    Group Name
                </p>
                <v-icon color="grey-lighten-4 d-none d-md-flex ">
                    mdi-circle-small
                </v-icon>
                <p class="text-body-1 text-yellow-darken-1 d-none d-md-flex">38 members</p>
            </div>
            <p class="text-caption text-grey-lighten-2">group description</p>
        </div>
        <div class="ml-auto">
            <v-btn icon size="42" class="bg-grey-darken-2">
                <v-icon>
                    mdi-dots-vertical
                </v-icon>
            </v-btn>
        </div>
    </div>
</template>

<script setup>

</script>

<style>
.gp_info_bx {
    height: 60px;
    background-color: rgba(255, 255, 255, 0.312) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    backdrop-filter: blur(4px) !important;
}
</style>