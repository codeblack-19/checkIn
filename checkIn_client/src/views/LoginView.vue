<template>
    <v-row no-gutters class="lg_bx">
        <v-col class="panel logo_display d-none d-md-flex flex-column align-center justify-center ">
            <img class="logo_gif" src="../assets/images/981-consultation-flat.gif" />
            <h2 class="text-h3 text-grey-lighten-2">checkIn msg.</h2>
        </v-col>
        <v-col class="panel d-flex flex-column align-center justify-center">
            <v-card class="fm_bx mx-auto px-6 py-8" width="320">
                <v-form v-model="form" @submit.prevent="onSubmit">
                    <div class="d-flex flex-column align-center justify-center mt-2">
                        <img class="d-lg-none logo_gif_md" src="../assets/images/981-consultation-flat.gif" />
                        <h3 class="text-h4 text-grey-lighten-1 text-center mb-3">Login</h3>
                    </div>

                    <p v-if="error" class="text-subtitle-1 text-center text-red-lighten-3 mb-2">{{error}}</p>

                    <v-text-field v-model="username" :readonly="loading" :rules="[required]"
                        class="mb-2 text-grey-lighten-5" clearable label="Username">
                    </v-text-field>

                    <v-text-field v-model="password" :readonly="loading" :rules="[required]" clearable label="Password"
                        class="text-grey-lighten-5">
                    </v-text-field>
                    <br>

                    <v-btn :disabled="!form" :loading="loading" block color="grey-lighten-5" size="large" type="submit"
                        variant="elevated">
                        Sign In
                    </v-btn>

                    <div class="d-flex justify-space-between mt-2">
                        <RouterLink to="/signup" class="text-grey-lighten-1 text-body-2">signUp</RouterLink>
                        <RouterLink to="/fpassword" class="text-grey-lighten-1 text-body-2">forgot password?</RouterLink>
                    </div>
                </v-form>
            </v-card>
        </v-col>
    </v-row>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import axios from 'axios'

const form = ref(false)
const username = ref(null)
const password = ref(null)
const loading = ref(false)
const error = ref(null)
const router = useRouter()

const onSubmit = () => {
    if (!form.value) return

    loading.value = true

    axios({
        method: 'POST',
        url:  `${import.meta.env.VITE_API_URL}/auth/login`,
        data: {
            username: username.value,
            password: password.value
        },
    }).then((res) => {
        // set session storage here
        console.log(res)

        // router.replace({path: '/'})
    }).catch((e) => {
        if(e.response.data){
            return error.value = e.response.data.detail
        }
    }).finally(() => {
        loading.value = false
    })

    // setTimeout(() => { loading.value = false }, 2000)
}

const required = (v) => {
    return !!v || 'Field is required'
}
</script>

<style>
.lg_bx {
    height: calc(100vh - 25px);
}

.panel {
    height: 100%;
}

.logo_gif {
    margin-top: -120px;
    width: 250px;
}

.logo_gif_md {
    width: 80px;
    margin: 0 auto;
}

.logo_display>h2 {
    margin-top: -30px;
}

.logo_display::after {
    position: absolute;
    right: 0;
    content: '';
    width: 1.5px;
    height: 80%;
    display: block;
    background-color: rgb(242, 242, 242);
}

.fm_bx {
    background-color: rgba(255, 255, 255, 0.149) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    backdrop-filter: blur(4px) !important;
}

.fm_bx h3 {
    margin-top: -15px;
}
</style>