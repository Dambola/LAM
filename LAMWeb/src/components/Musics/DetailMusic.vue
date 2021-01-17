<template>
  <q-card>

    <!-- Music Header -->
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

    <!-- Music Session -->
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

      <!-- Type Session -->
      <div class="row q-mt-sm">
        <div class="col">
          <div class="row">
            <div class="col"><span class="text-subtitle2">Tipo:</span></div>
          </div>
          <div class="row text-center">
            <div class="col"><small>{{ music.type1 ? music.type1 : '-' }}</small></div>
            <div class="col"><small>{{ music.type2 ? music.type2 : '-' }}</small></div>
            <div class="col"><small>{{ music.type3 ? music.type3 : '-' }}</small></div>
          </div>
        </div>
      </div>

      <!-- Actions Session -->
      <div class="row text-center q-pt-lg">
        <div class="col">
          <q-btn 
            icon="fas fa-trash-alt" 
            size="sm" 
            class="q-mx-md text-white bg-red-6" 
            @click="deleteThisMusic"
            v-if="canDeleteMusic"
          />
          <q-btn 
            icon="fas fa-edit" 
            size="sm" 
            class="q-mx-md text-white bg-yellow-6" 
            @click="openEditMusic"
            v-if="canEditMusic"
          />
          <!-- <q-btn 
            icon="fas fa-external-link-square-alt" 
            size="sm" 
            class="q-mx-md text-white bg-green-13" 
          /> -->
        </div>
      </div>

    </q-card-section>
  </q-card>
</template>

<script>
  import { mapActions } from 'vuex';

  export default {
    data () {
      return {}
    },
    methods: {
      ...mapActions('musics',['deleteMusic']),
      openEditMusic () {
        this.$emit('openEditMusic',this.id);
      },

      deleteThisMusic () {
        this.deleteMusic(this.id);
        this.$emit('close');
      }
    },
    props: ['music','id','canEditMusic','canDeleteMusic']
  };
</script>

<style lang="scss">

</style>