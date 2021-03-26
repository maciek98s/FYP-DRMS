<template>
<ion-app>
    <ion-content fullscreen class="ion-padding" scroll-y="false">

      <ion-slides>

        <ion-slide>
          <div class="slide">
            <img src="../images/eye3.png"/>
            <h1>Welcome</h1>
            <p>To <b> DRMS </b> also known as Diabetic Retinopathy Monitoring System </p> <br>
            <p> ( Swipe left for next slide ) </p>
          </div>
        </ion-slide>

        <ion-slide>
          <img src="../images/app.png"/>
          <h2>What is DRMS</h2>
          <p><b>DRMS</b> is an application which helps to predecit for diabetic retinopathy from an image taken with a D-eye sensor</p> <br>
          <p> ( Swipe left for next slide ) </p>
        </ion-slide>

        <ion-slide>
          <img src="../images/D-EYE.png"/>
          <h2>What's a D-eye sensor </h2>
          <p><b>The D-eye sensor </b>is a powerfull tool that allows us to look into our own retinas from home </p>
          <p>the used of the sensor requires some Guidence if this is your first time using the app Clikc the Tutorial button otherwise click Get Started </p>
           <ion-button fill="clear">Tutorial</ion-button>
           <ion-button fill="clear">Get Started</ion-button>
        </ion-slide>

        <ion-slide>
          <img src=""/>
          <h2>Ready to Play?</h2>
          <ion-button fill="clear">Continue <ion-icon slot="end" name="arrow-forward"></ion-icon></ion-button>
        </ion-slide>

      </ion-slides>
    </ion-content>
  </ion-app>
</template>


<script>
import { IonSlides, IonSlide } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
  components: { IonSlides, IonSlide },
  setup() {
    // Optional parameters to pass to the swiper instance. See http://idangero.us/swiper/api/ for valid options.
    const slideOpts = {
      initialSlide: 1,
      speed: 400
    };
    return { slideOpts }
  }
});
</script>
<style>
    ion-slides {
      height: 100%;
    }

    .swiper-slide {
      display: block;
    }

    .swiper-slide h2 {
      margin-top: 2.8rem;
    }

    .swiper-slide img {
      max-height: 50%;
      max-width: 80%;
      margin: 60px 0 40px;
      pointer-events: none;
    }

    b {
      font-weight: 500;
    }

    p {
      padding: 0 40px;
      font-size: 14px;
      line-height: 1.5;
      color: var(--ion-color-step-600, #60646b);
    }

    p b {
      color: var(--ion-text-color, #000000);
    }
  </style>