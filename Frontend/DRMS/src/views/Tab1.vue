<template>
  <ion-app>
    <ion-content fullscreen class="ion-padding" scroll-y="true">
      <ion-header>
        <ion-toolbar>
          <ion-title style="text-align: center;">Prediction Page</ion-title>
          <ion-buttons slot="start">
            <ion-back-button
            
              @click="() => router.push('/Tutorial')"
              default-href="home"
            > 
              <a href="/Tutorial"></a>
            </ion-back-button>
              Tutorial
          </ion-buttons>
        </ion-toolbar>
      </ion-header>
      <div class="item images-parent your-img">
        <img src="../images/example.jpg" class="center-image" /><br />
        <label
          >This is an Example photo Of a Picture of a Retina Obtained with the
          D-eye Sensor </label
        ><br /><br /><br />
        <h3>Select File</h3>
        <p>
          Select an image that will contain a picture of a retina for prediction
          of Diabetic Retinopathy
        </p>
        <label class="custom-file-upload"
          >Upload Imageionic
          <input
            type="file"
            id="file"
            ref="file"
            v-on:change="handleFileUpload()"
          /> </label
        ><br />
        <ion-button color="light" @click="submitFile"> Send Image </ion-button>
      </div>
      <ion-fab vertical="bottom" horizontal="end" slot="fixed">
        <ion-fab-button @click="takePhoto()">
          <ion-icon :icon="camera"></ion-icon>
        </ion-fab-button>
      </ion-fab>
    </ion-content>
  </ion-app>
</template>
<script>
import axios from "axios";
import {
  IonHeader,
  IonTitle,
  IonFab,
  IonFabButton,
  IonContent,
  IonToolbar,
  IonButton,
  alertController,
} from "@ionic/vue";
import { camera, trash, close, arrowBack } from "ionicons/icons";
import { usePhotoGallery } from "@/composables/usePhotoGallery";
import { useRouter } from "vue-router";
import { defineComponent } from "vue";

export default defineComponent({
  components: {
    IonTitle,
    IonFab,
    IonFabButton,
    IonHeader,
    IonButton,
    IonToolbar,
    IonContent,
  },
  setup() {
    const { takePhoto } = usePhotoGallery();
    const router = useRouter();
    return {
      takePhoto,
      camera,
      trash,
      close,
      arrowBack,
      router,
    };
  },
  data() {
    return {
      previewImageUrl: "",
      file: "",
      info: null,
      predict: "null",
      selected: "",
    };
  },
  mounted() {
    this.presentAlert()
  },
  methods: {
    async presentAlert() {
      const alert = await alertController
        .create({
          cssClass: 'my-custom-class',
          header: 'Welcome',
          subHeader: 'This is the Prediction page',
          message: 'Here you can submit you image for a prediction of Diabetic Retinopathy <br> Its suggested to visit the tutorial page before accessing this one <br>  if you wish to viti the tutorial page click the arrow in the top right corner ',
          buttons: ['OK'],
        });
      return alert.present();    
  },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
      this.selected = this.file.name;
      console.log(this.file.name);
    },
    async submitFile() {
      /*
                Initialize the form data
            */
      const formData = new FormData();

      /*
                Add the form data we need to submit
            */
      formData.append("file", this.file);

      /*
          Make the request to the POST /single-file URL
        */
      axios
        .post("http://localhost:5000/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => (this.predict = response.data))
        .catch(function() {
          console.log("FAILURE!!");
        });
      if (this.predict == "null") {
        this.predict = "No prediction was made please upload  an image ";
      }

      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: "Result",
        subHeader: "Prediction",
        message: "The System has predicted that : " + this.predict,
        buttons: ["Close"],
      });
      return alert.present();
    },
    link() {
      window.open("https://www.w3schools.com");
    },
  },
});
</script>
<style scoped>
.images-parent {
  text-align: center;
}
.center-image {
  padding-top: 20px;
  margin: 0 auto;
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
.your-img {
    border-radius: 10px !important;
    overflow: hidden;
}
</style>
