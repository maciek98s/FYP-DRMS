<template>
    <ion-page>
       <ion-content fullscreen class="ion-padding" scroll-y="false">
          <div class="item images-parent">
            <img src="../images/example.jpg" class="center-image"><br>
            <label>This is an Example photo Of a Picture of a Retina Obtained with the D-eye Sensor </label><br><br><br>
            <h3>Select File </h3>
            <p>Select an image that will contain a picture of a retina for prediction of Diabetic Retinopathy</p>
            <label class="custom-file-upload">Upload Image
              <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
            </label><br>
            <ion-button color="light" @click="submitFile"> Send Image </ion-button>
        
          </div>
        <ion-fab vertical="bottom" horizontal="center" slot="fixed">
        <ion-fab-button @click="takePhoto()">
        <ion-icon :icon="camera"></ion-icon>
        </ion-fab-button>
      </ion-fab>
       </ion-content>
    </ion-page>
</template>
<script>
import axios from 'axios';
import { IonPage,IonHeader, IonTitle,IonFab,IonFabButton, IonContent, IonToolbar,  IonButton, IonIcon,  alertController, IonGrid, IonRow,IonCol, IonImg, IonThumbnail } from '@ionic/vue';
import { camera, trash, close } from 'ionicons/icons';
import { usePhotoGallery} from '@/composables/usePhotoGallery';



export default {
  
    components: {
       // IonPage,
        //IonHeader,
        //IonTitle,
        //IonContent,
        //IonToolbar,
        //IonThumbnail,
        //IonButton,
        //IonIcon,
        //IonItem,
        IonFab,
        IonFabButton,
        //IonGrid,
        //IonImg,
        //IonCol,
       // IonRow,
    },
    setup(){
      const { takePhoto } = usePhotoGallery();
      return {
          takePhoto,
          camera, trash, close
     }

    },
    data(){
        return {
            previewImageUrl: '',
            file: '',
            info: null,
            predict: "null",
            selected: ''
        }
    },
    mounted() {
        axios.get('http://localhost:5000/').then(response => (this.info = response))
        console.log(this.predict)

    },
    methods: {
        handleFileUpload(){
            this.file = this.$refs.file.files[0];
            this.selected = this.file.name
            console.log(this.file.name)

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
            ).then(response => (this.predict = response.data))
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
<style scoped>

.images-parent{
      text-align: center;
}
.center-image{
      padding-top: 100px;
      margin:0 auto;
      max-width: 300px !important;
      max-height: 300px !important;
}
input[type="file"] {
    display: none;
}
.custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}


</style>