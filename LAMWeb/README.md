# LAM (lam)

Louvor Ágape Montese Application

## Install the dependencies
```bash
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```


### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.conf.js](https://quasar.dev/quasar-cli/quasar-conf-js).

### Sign a APK
#### Generate Key
keytool -genkey -v -keystore mykey.keystore -alias MyKey -keyalg RSA -keysize 2048 -validity 10000

#### Sign the APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore mykey.keystore app-release-unsigned.apk MyKey