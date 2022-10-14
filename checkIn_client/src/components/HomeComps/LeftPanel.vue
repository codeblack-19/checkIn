<template>
    <v-col lg="3" class="left-panel panel d-flex flex-column">
        <div class="gp_head px-3 py-2 d-flex flex-column mb-1 align-center">
            <h5 class="text-grey-lighten-4 text-subtitle-2">Groups de'la checkIn</h5>
            <p class="text-grey-lighten-1 font-italic text-caption">Select a group to join or chat</p>
        </div>

        <v-row no-gutters class="gp_list overflow-y-auto">
            <v-col lg="12">
                <v-card v-for="n in 0" :key="n" class="pa-2 mb-1" outlined tile>
                    Group name
                </v-card>
            </v-col>
        </v-row>
    </v-col>
</template>

<script setup>

</script>

<style>
/* .left-panel .v-card {
    background-color: rgba(255, 255, 255, 0.312) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    backdrop-filter: blur(4px) !important;
} */

.gp_head {
    height: 61px;
    background-color: rgba(255, 255, 255, 0.312) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    backdrop-filter: blur(4px) !important;
}

.left-panel .gp_list {
    position: relative;
    height: calc(100% - 55px);
    background-color: rgba(255, 255, 255, 0.312) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    backdrop-filter: blur(4px) !important;
}

.gp_list::-webkit-scrollbar {
    width: 5px;
}

.gp_list::-webkit-scrollbar-thumb {
    padding: 0 1px;
    border-left: 2px solid transparent;
    background: rgba(245, 245, 245, 0.564);
    background-clip: padding-box;
    border-radius: 100px;
}
</style>