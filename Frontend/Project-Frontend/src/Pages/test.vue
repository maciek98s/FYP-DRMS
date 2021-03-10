<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-title>Page</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content>
            <ion-item>
                <ion-thumbnail >
                    <img type="file" id="file" ref="file" :src="previewImageUrl " v-on:change="handleFileUpload()" />
                </ion-thumbnail>
                <ion-button fill="clear" @click="takePhoto">
                    <ion-icon slot="start" :icon="camera"></ion-icon>
                    Take Photo
                </ion-button>
                <ion-button v-on:click="submitFile()">
                    Submit
                </ion-button>
            </ion-item>
        </ion-content>
    </ion-page>
</template>
<script>
import axios from 'axios';
import { IonPage,IonHeader, IonTitle, IonContent, IonToolbar, IonThumbnail, IonButton, IonIcon, IonItem } from '@ionic/vue';
import { camera } from 'ionicons/icons';
import { Plugins, CameraResultType, CameraSource } from '@capacitor/core';

const { Camera} = Plugins;

export default {
    components: {
        IonPage,
        IonHeader,
        IonTitle,
        IonContent,
        IonToolbar,
        IonThumbnail,
        IonButton,
        IonIcon,
        IonItem,
    },
    data(){
        return {
            camera,
            previewImageUrl: '',
            file: '',
        }
    },
    methods: {
        async takePhoto() {
            const photo = await Camera.getPhoto({
                resultType: CameraResultType.Uri,
                source: CameraSource.Camera,
                quality: 100
            });

            this.previewImageUrl = photo.webPath;
        },
        handleFileUpload(){
            this.file = this.$refs.file.files[0];
            print("bob");

        },
        submitFile(){
        /*
                Initialize the form data
            */
            let formData = new FormData();

            /*
                Add the form data we need to submit
            */
            formData.append('file', this.file);

        /*
          Make the request to the POST /single-file URL
        */
            axios.post( 'http://127.0.0.1:5000/poo',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
      },

    }
}
</script>