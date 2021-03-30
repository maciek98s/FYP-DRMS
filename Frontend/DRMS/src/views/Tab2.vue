<template>
  <ion-app>
    <ion-content fullscreen class="ion-padding" scroll-y="true">
      <ion-header>
        <ion-toolbar>
          <ion-title style="text-align: center;">Prediction Page</ion-title>
        </ion-toolbar>
      </ion-header>
      <div class="item images-parent">
        <ion-card>
          <ion-card-header>
            <ion-card-subtitle>Card Subtitle</ion-card-subtitle>
            <ion-card-title>Welcome To the Tutorial Page </ion-card-title>
          </ion-card-header>

          <ion-card-content>
            This is the Tutorial Page, here you will find buttons that will
            bring you to videos describing how to app works. The Videos range
            from Tutorials describing how set up D-eye sensor, Using D-eye
            sensor and Getting an accurate Retinal Image.
          </ion-card-content>
        </ion-card>
        <img src="../images/D-EYE.png" class="center-image" /><br />
        <label>Setting up the D-eye sensor</label><br />
        <ion-button
          size="small"
          color="light"
          @click="() => router.push('/Prediction')"
        >
          View Tutorial </ion-button
        ><br />
        <img src="../images/camera.png" class="center-image" /><br />
        <label>Capturing Retina Image using D-eye sensor</label><br />
        <ion-button size="small" color="light"> View Tutorial </ion-button
        ><br />
        <img src="../images/upload.png" class="center-image" /><br />
        <label>Uploading appropriate image to the app </label><br />
        <ion-button size="small" color="light" @click="wsfsfs">
          View Tutorial </ion-button
        ><br />
        <ion-button @click="() => router.push('/Prediction')" fill="clear"
          ><a href="/Prediction">Exit Tutorials</a></ion-button
        >
      </div>
    </ion-content>
  </ion-app>
</template>

<script lang="ts">
import { camera, trash, close } from "ionicons/icons";
import {
  IonCard,
  IonCardContent,
  IonCardTitle,
  IonContent,
} from "@ionic/vue";
import { usePhotoGallery } from "@/composables/usePhotoGallery";
import { useRouter } from "vue-router";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Tab2",
  components: {
    IonContent,
    IonCard,
    IonCardContent,
    IonCardTitle,

  },
  setup() {
    const { takePhoto } = usePhotoGallery();
    const router = useRouter();
    return {
      takePhoto,
      camera,
      trash,
      close,
      router,
    };
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
  max-width: 200px !important;
  max-height: 200px !important;
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
