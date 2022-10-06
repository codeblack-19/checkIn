<template>
    <div class="gp_info_bx px-3 py-2 d-flex">
        <v-avatar color="grey-lighten-5" size="42" class="bg-grey-darken-1 mr-2">
            <v-icon dark>
                mdi-account-multiple
            </v-icon>
        </v-avatar>
        <div class="d-flex flex-column">
            <div class="d-flex">
                <p class="text-subtitle-2 text-grey-lighten-4">
                    Group Name
                </p>
                <v-icon color="grey-lighten-4">
                    mdi-circle-small
                </v-icon>
                <p class="text-body-1 text-yellow-darken-1">38 members</p>
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