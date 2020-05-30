<template>
  <q-page class="row items-center justify-evenly" padding>
    <q-markup-table 
      class="lam-table-music col-12" 
      :wrap-cells="true"
      v-if="Object.keys(musics).length"
    >
      <thead>
        <tr>
          <th class="text-left">
            Música
          </th>
          <th class="text-right">Típos</th>
        </tr>
      </thead>
      <tbody>
        <music
          v-for="(music, key) in musics"
          :key="key"
          :music="music"
          :id="key"
        >
        </music>
      </tbody>
    </q-markup-table>

    <div class="absolute-bottom text-center q-mb-lg">
      <q-btn 
        round 
        icon="add"
        color="primary"
        size="20px"
        @click.stop="showAddTask = true"
        dense 
      />
    </div>

    <q-dialog v-model="showAddTask">
      <add-music @close="showAddTask = false"/>
    </q-dialog>
  </q-page>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'Músicas',
    computed: {
      ...mapGetters('musics', ['musics'])
    },
    components: {
      'music' : require('components/Musics/Music.vue').default,
      'add-music' : require('components/Musics/AddMusic.vue').default
    },
    data () {
      return {
        showAddTask: false
      }
    },
    methods : {
    }
  }
</script>

<style lang="scss">
.lam-table-music {
  margin: 25px 0px;
  white-space: normal !important;
  thead > tr {
    background-color: $lam-music-header;
    color: white;
    th {
      font-size: 20px;
      font-weight: 1000;
      padding-top: 15px;
      padding-bottom: 15px;
    }
  }
  tbody > tr:nth-child(2n) { background-color: $lam-music-even; }
  tbody > tr:nth-child(2n+1) { background-color: $lam-music-odd ; }
  tbody > tr:hover { background-color: $lam-music-hover ; }
}
</style>