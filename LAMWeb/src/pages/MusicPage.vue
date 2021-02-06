<template>
  <q-page class="row items-center justify-evenly" padding>
    <q-markup-table 
      class="lam-table-music col-12" 
      :wrap-cells="true"
    >
      <thead>
        <tr>
          <th class="text-left relative-position">
            <q-btn 
              round 
              icon="add"
              color="white"
              text-color="primary"
              class="absolute-center"
              @click.stop="showAddMusic = true"
              dense 
              v-if="canAddMusic()"
            />
            Música
          </th>
          <th class="text-right">
            Típos
          </th>
        </tr>
      </thead>
      <tbody>
        <music
          v-for="(music, key) in musics"
          :key="key"
          :music="music"
          :id="key"
          @openDetailMusic="openDetailMusic"
        >
        </music>
      </tbody>
    </q-markup-table>

    <q-dialog v-model="showAddMusic">
      <add-music @close="showAddMusic = false"/>
    </q-dialog>

    <q-dialog v-model="showDetailMusic" :full-width="true">
      <detail-music 
        :music="getMusicInfo(clickedMusic)"
        :id="clickedMusicID"
        :canEditMusic="canEditMusic()"
        :canDeleteMusic="canDeleteMusic()"
        @openEditMusic="openEditMusic"
        @close="showDetailMusic = false"
      />
    </q-dialog>

    <q-dialog v-model="showEditMusic" :full-width="true">
      <edit-music 
        :music="getMusicInfo(clickedMusic)"
        :id="clickedMusicID"
        @close="showEditMusic = false"
      />
    </q-dialog>
  </q-page>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'Músicas',
    computed: {
      ...mapGetters('musics', ['musics']),
      ...mapGetters('types', ['types']),
      ...mapGetters('permissions', ['permissions']),
    },

    components: {
      'music' : require('components/Musics/Music.vue').default,
      'add-music' : require('components/Musics/AddMusic.vue').default,
      'detail-music' : require('components/Musics/DetailMusic.vue').default,
      'edit-music' : require('components/Musics/EditMusic.vue').default
    },

    data () {
      return {
        showAddMusic: false,
        showDetailMusic: false,
        showEditMusic: false,
        clickedMusicID: -1,
        clickedMusic: null
      }
    },
    methods : {
      openDetailMusic (index) {
        this.clickedMusicID = index;
        this.clickedMusic = this.musics[index];
        this.showAddMusic = false;
        this.showEditMusic = false;
        this.showDetailMusic = true;
      },

      openEditMusic (index) {
        this.clickedMusicID = index;
        this.clickedMusic = this.musics[index];
        this.showAddMusic = false;
        this.showDetailMusic = false;
        this.showEditMusic = true;
      },

      getMusicInfo (music) {
        if (!music) return null;
        return {
          name: music.name,
          author: music.author,
          type1: this.types[music.type1] ? this.types[music.type1].name : null,
          type2: this.types[music.type2] ? this.types[music.type2].name : null,
          type3: this.types[music.type3] ? this.types[music.type3].name : null,
        }
      },

      canAddMusic () { return this.permissions.indexOf(this.$perms.ADD_MUSIC) != -1; },
      canEditMusic () { return this.permissions.indexOf(this.$perms.EDT_MUSIC) != -1; },
      canDeleteMusic () { return this.permissions.indexOf(this.$perms.DEL_MUSIC) != -1; },

      ...mapActions('permissions', ['reloadPermissions']),
      ...mapActions('types', ['reloadTypes']),
      ...mapActions('musics', ['reloadMusics']),
    },

    mounted () {
      this.reloadPermissions();
      this.reloadTypes();
      this.reloadMusics();
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