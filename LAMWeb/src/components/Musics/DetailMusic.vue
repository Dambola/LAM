<template>
  <q-card>
    <q-card-section class="row">
      <div class="text-h6">Música</div>
      <q-space />
      <q-btn 
        flat
        round
        dense
        v-close-popup
        icon="close"
      />
    </q-card-section>
    <q-card-section class="q-pt-none">
      <div class="row">
        <div class="col q-mr-sm">
          <div class="row">
            <span class="text-subtitle2">Nome:</span>
          </div>
          <div class="row">
            <small>{{ music.name }}</small>
          </div>
        </div>
        <div class="col">
          <div class="row">
            <span class="text-subtitle2">Autor:</span>
          </div>
          <div class="row">
            <small>{{ music.author }}</small>
          </div>
        </div>
      </div>
      <div class="row q-mt-sm">
        <div class="col">
          <div class="row">
            <div class="col"><span class="text-subtitle2">Tipo:</span></div>
          </div>
          <div class="row">
            <div class="col text-center"><small>{{ music.type1 ? music.type1 : '-' }}</small></div>
            <div class="col text-center"><small>{{ music.type2 ? music.type2 : '-' }}</small></div>
            <div class="col text-center"><small>{{ music.type3 ? music.type3 : '-' }}</small></div>
          </div>
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
  export default {
    data () {
      return {}
    },
    methods: {},
    props: ['music']
  }
</script>

<style lang="scss">

</style>