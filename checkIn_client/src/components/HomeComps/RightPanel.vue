<template>
    <v-col lg="9" class="right-panel panel pl-1">
        <!-- panel header -->
        <RpHeader />

        <!-- chat area -->
        <div class="chat_bx">
            
        </div>

        <!-- text box (input field) -->
        <div>

        </div>
    </v-col>
</template>

<script setup>
import RpHeader from './PanelComps/RpHeader.vue';

</script>

<style>
.chat_bx {
    height: calc(100% - 140px);
    background-color: rgba(255, 255, 255, 0.216) !important;
    -webkit-backdrop-filter: blur(2px) !important;
    backdrop-filter: blur(2px) !important;
}
</style>