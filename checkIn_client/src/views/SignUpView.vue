<template>
    <div class="sign_up_bx">
        <v-card class="fm_bx mx-auto px-6 py-8" width="320">
            <v-form v-model="form" @submit.prevent="onSubmit">
                <div class="d-flex flex-column align-center justify-center">
                    <img class="logo_gif_md" src="../assets/images/981-consultation-flat.gif" />
                    <h3 class="text-h4 text-grey-lighten-1 text-center mb-3">Sign Up</h3>
                </div>

                <p v-if="error" class="text-subtitle-1 text-center text-red-lighten-3 mb-2">{{error}}</p>
        
                <v-text-field v-model="email" :readonly="loading" :rules="[required]" class="text-grey-lighten-5"
                    clearable label="Email">
                </v-text-field>

                <v-text-field v-model="username" :readonly="loading" :rules="[required]" class="text-grey-lighten-5" clearable
                    label="Username">
                </v-text-field>
        
                <v-text-field v-model="password" :readonly="loading" :rules="[required]" clearable label="Password"
                    class="text-grey-lighten-5">
                </v-text-field>

                <v-text-field v-model="cpassword" :readonly="loading" :rules="[required, checkPass]" clearable label="Confirm Password"
                    class="text-grey-lighten-5">
                </v-text-field>
        
                <v-btn :disabled="!form" :loading="loading" block color="grey-lighten-5" size="large" type="submit"
                    variant="elevated" class="mt-4">
                    Sign Up
                </v-btn>

                <div class="d-flex justify-space-between mt-2">
                    <RouterLink to="/login" class="text-grey-lighten-1 text-body-2">login</RouterLink>
                    <RouterLink to="/fpassword" class="text-grey-lighten-1 text-body-2">forgot password?</RouterLink>
                </div>
            </v-form>
        </v-card>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import axios from 'axios';
const form = ref(false)
const email = ref(null)
const username = ref(null)
const password = ref(null)
const cpassword = ref(null)
const loading = ref(false)
const error = ref('error')
const router = useRouter()

const onSubmit = () => {
    if (!form.value) return

    loading.value = true

    axios({
        method: 'POST',
        url:  `${import.meta.env.VITE_API_URL}/auth/register`,
        data: {
            username: username.value,
            email: email.value,
            password: password.value,
            password2: cpassword.value
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
    // router.replace({path: '/'})
}

const checkPass = () => {
    if (cpassword.value !== password.value) {
        return 'password does not match'
    }else{
        return true
    }
}

const required = (v) => {
    return !!v || 'Field is required'
}

</script>

<style>
.sign_up_bx{
    height: 100vh;
    display: grid;
    place-content: center;
}

.fm_bx {
    border: .5px solid rgba(245, 245, 245, 0.455);
    background-color: rgba(0, 0, 0, 0.132) !important;
    -webkit-backdrop-filter: blur(6px) !important;
    backdrop-filter: blur(6px) !important;
}

.fm_bx h3 {
    margin-top: -15px;
}
.logo_gif_md {
    width: 80px;
    margin: 0 auto;
}
</style>