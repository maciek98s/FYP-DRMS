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
                    <imgn :src="previewImageUrl" />
                </ion-thumbnail>
                <ion-button fill="clear" @click="takePhoto">
                    <ion-icon slot="start" :icon="camera"></ion-icon>
                    Take Photo
                </ion-button>
                      <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
     
                
            </ion-item>
                <ion-button @click="submitFile"> Submit </ion-button>
        </ion-content>
        <div> {{ info }} </div>
    </ion-page>
</template>
<script>
import axios from 'axios';
import { IonPage,IonHeader, IonTitle, IonContent, IonToolbar, IonThumbnail, IonButton, IonIcon, IonItem, alertController } from '@ionic/vue';
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
            info: null,
        }
    },
    mounted() {
        axios.get('https://fae76f10df68.ngrok.io').then(response => (this.info = response))


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
            print(this.file);

        },
        async submitFile(){
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
            axios.post( 'https://fae76f10df68.ngrok.io',
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
        const alert = await alertController
        .create({
          cssClass: 'my-custom-class',
          header: 'Alert',
          subHeader: 'Subtitle',
          message: 'This is an alert message.',
          buttons: ['OK'],
        });
      return alert.present();
      },

    }
}
</script>