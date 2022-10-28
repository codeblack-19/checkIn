<template>
    <v-col class="left-panel panel d-none d-md-flex flex-column">
        <div class="gp_head px-3 py-2 d-flex flex-column mb-1 align-center">
            <h5 class="text-grey-lighten-4 text-subtitle-2">Groups de'la checkIn</h5>
            <p class="text-grey-lighten-1 font-italic text-caption">Select a group to join or chat</p>
        </div>

        <v-row no-gutters align-content="start" class="gp_list overflow-y-auto pb-2">
            <v-col lg="12" md="12" v-for="n in 3" :key="n">
                <v-hover
                    v-slot="{ isHovering, props }"
                >
                    <v-card 
                        v-bind="props" 
                        :color="isHovering ? 'grey-darken-1' : 'grey-lighten-1'" 
                        class="pa-2 my-3 mx-2 d-flex group_card"
                    >
                        <v-avatar :color="isHovering ? 'grey-darken-2' : 'grey-darken-1'" size="48">
                            <v-icon dark>
                                mdi-account-multiple
                            </v-icon>
                        </v-avatar>
                        <div class="ml-2">
                            <p class="text-body-1 font-weight-medium">Group Name</p>
                            <p class="text-body-2">
                                Description
                            </p>
                        </div>
                    </v-card>
                </v-hover>
                
                <v-divider class="bg-grey-lighten-1 mx-2"></v-divider>
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

.group_card{
    cursor: pointer;
}
</style>