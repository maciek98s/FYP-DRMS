import { ref, onMounted, watch } from 'vue';
import { Plugins, CameraResultType, CameraSource, CameraPhoto, Capacitor, FilesystemDirectory } from "@capacitor/core";
import { isPlatform } from '@ionic/vue';

export function usePhotoGallery() {
    const { Camera, Filesystem, Storage } = Plugins;



    const takePhoto = async () => {
        const cameraPhoto = await Camera.getPhoto({
            resultType: CameraResultType.Uri,
            source: CameraSource.Camera,
            saveToGallery: true,
            quality: 100
        });
        const fileName = new Date().getTime() + '.jpeg';
        
    };

    return {
        takePhoto,
    }
}
