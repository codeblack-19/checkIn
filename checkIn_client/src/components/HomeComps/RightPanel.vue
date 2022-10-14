<template>
    <v-col lg="9" class="right-panel panel pl-1">
        <!-- panel header -->
        <RpHeader />

        <!-- chat area -->
        <div class="chat_bx px-4 py-3 overflow-y-auto">
            <div 
                v-for="n in 10" :key="n" 
                :class="`chat_msg rounded-xl py-3 px-3 mb-2 ${n%3 === 0 ? 'sender float-right bg-grey-lighten-5 rounded-be-0' : `other float-left bg-blue-grey-darken-2 ${(n-1) % 3 === 0 ? 'rounded-bs-0' : 'rounded-ts-0' }`}`"
            >
                <h4 v-if="n%3!==0" 
                    :class="`text-orange-lighten-1`"
                >
                    other 
                </h4>
                
                <p :class="`text-body-2`">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Soluta quis, amet nemo nihil neque omnis. Porro molestiae
                    dolor, suscipit ducimus sequi ex magni exercitationem et blanditiis sed, commodi eius rerum.
                </p>
                <p class="text-right text-caption">
                    {{new Date().toLocaleTimeString()}}
                </p>
            </div>
        </div>

        <!-- text box (input field) -->
        <div v-if="isMember" class="input_bx d-flex pr-2 align-center bg-grey-lighten-4">
            <textarea
                placeholder="Enter message here"
                class="bg-grey-lighten-4 pa-2 mr-2"
            ></textarea>
            <div class="ml-auto">
                <v-btn icon size="42" class="bg-grey-lighten-3">
                    <v-icon>
                        mdi-send
                    </v-icon>
                </v-btn>
            </div>
        </div>
        <div v-else class="input_bx d-flex pr-2 justify-center align-center bg-grey-darken-4">
            <v-btn class="bg-grey-lighten-3">
                Click Here to Join Group
            </v-btn>
        </div>
    </v-col>
</template>

<script setup>
import { ref } from 'vue';
import RpHeader from './PanelComps/RpHeader.vue';

const isMember = ref(false)

</script>

<style>
.chat_bx {
    height: calc(100% - 115px);
    background-color: rgba(255, 255, 255, 0.064) !important;
    -webkit-backdrop-filter: blur(2px) !important;
    backdrop-filter: blur(2px) !important;
}

.chat_bx::-webkit-scrollbar {
    width: 5px;
}

.chat_bx::-webkit-scrollbar-thumb {
    padding: 0 1px;
    border-left: 2px solid transparent;
    background: rgba(245, 245, 245, 0.564);
    background-clip: padding-box;
    border-radius: 100px;
}

.chat_msg{
    position: relative;
    border: 1px solid rgba(128, 128, 128, 0.414);
    max-width: 70%;
}

/* input area */
.input_bx{
    height: 55px;
    position: relative;
}

.input_bx > textarea{
    height: 100% !important;
    flex: 1;
    outline: none;
    font-size: 14px;
    resize: none;
}
</style>