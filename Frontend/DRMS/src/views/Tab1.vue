<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-title>Page</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content :fullscreen="true">
            <ion-grid>
    <ion-row>

    </ion-row>
  </ion-grid>
            <ion-fab vertical="bottom" horizontal="center" slot="fixed">
              <ion-fab-button @click="takePhoto()">
                <ion-icon :icon="camera"></ion-icon>
              </ion-fab-button>
            </ion-fab>
         <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>

          <ion-button @click="submitFile"> Submit </ion-button>
        </ion-content>
        <div> {{ info }} </div>
    </ion-page>
</template>
<script>
import axios from 'axios';
import { IonPage,IonHeader, IonTitle,IonFab,IonFabButton, IonContent, IonToolbar,  IonButton, IonIcon,  alertController, IonGrid, IonRow,IonCol, IonImg } from '@ionic/vue';



export default {
  
    components: {
        IonPage,
        IonHeader,
        IonTitle,
        IonContent,
        IonToolbar,
        //IonThumbnail,
        IonButton,
        IonIcon,
        //IonItem,
        IonFab,
        IonFabButton,
        IonGrid,
        //IonImg,
        //IonCol,
        IonRow,
    },
    data(){
        return {
            previewImageUrl: '',
            file: '',
            info: null,
        }
    },
    mounted() {
        axios.get('http://localhost:5000/').then(response => (this.info = response))

    },
    methods: {
        handleFileUpload(){
            this.file = this.$refs.file.files[0];
            print(this.file);

        },
        async submitFile(){

        /*
                Initialize the form data
            */
            const formData = new FormData();

            /*
                Add the form data we need to submit
            */
            formData.append('file', this.file);

        /*
          Make the request to the POST /single-file URL
        */
            axios.post( 'http://localhost:5000/',
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