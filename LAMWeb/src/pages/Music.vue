<template>
  <q-page class="row items-center justify-evenly" padding>
    <q-markup-table class="lam-table-music col-12" :wrap-cells="true">
      <thead>
        <tr>
          <th class="text-left">Música</th>
          <th class="text-right">Típos</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(music, index) in musics"
          :key="index"
        >
          <td class="text-left" @click="musicModalShow()">
            <div class="text-subtitle1"><strong>{{ music.name }}</strong></div>
            <small>{{ music.author }}</small>
          </td>
          <td class="text-right">
            <div>{{ music.type1 }}</div>
            <div>{{ music.type2 }}</div>
            <div>{{ music.type3 }}</div>
          </td>
        </tr>
      </tbody>
    </q-markup-table>
    <!-- <q-pagination
      v-model="page"
      :max="15"
      :max-pages="5"
      :direction-links="true"
    >
    </q-pagination> -->
  </q-page>
</template>

<script>
export default {
  name: 'Músicas',
  computed: {},
  components: {},
  data () {
    return {
      page : 1,
      musics : [
        {
          name : 'Eu navegarei',
          author : 'Gabriela Rocha',
          type1 : 'Adoração',
          type2 : null,
          type3 : null
        },
        {
          name : 'Lugar secreto',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Louvor',
          type3 : null
        },
        {
          name : 'Atos 2',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Júbilo',
          type3 : 'Adoração'
        },
        {
          name : 'Creio que Tu és a cura',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Adoração',
          type3 : null
        },
        {
          name : 'Eu navegarei',
          author : 'Gabriela Rocha',
          type1 : 'Adoração',
          type2 : null,
          type3 : null
        },
        {
          name : 'Lugar secreto',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Louvor',
          type3 : null
        },
        {
          name : 'Atos 2',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Júbilo',
          type3 : 'Adoração'
        },
        {
          name : 'Creio que Tu és a cura',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Adoração',
          type3 : null
        },
        {
          name : 'Eu navegarei',
          author : 'Gabriela Rocha',
          type1 : 'Adoração',
          type2 : null,
          type3 : null
        },
        {
          name : 'Lugar secreto',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Louvor',
          type3 : null
        },
        {
          name : 'Atos 2',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Júbilo',
          type3 : 'Adoração'
        },
        {
          name : 'Creio que Tu és a cura',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Adoração',
          type3 : null
        },
        {
          name : 'Eu navegarei',
          author : 'Gabriela Rocha',
          type1 : 'Adoração',
          type2 : null,
          type3 : null
        },
        {
          name : 'Lugar secreto',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Louvor',
          type3 : null
        },
        {
          name : 'Atos 2',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Júbilo',
          type3 : 'Adoração'
        },
        {
          name : 'Creio que Tu és a cura',
          author : 'Gabriela Rocha',
          type1 : 'Oração',
          type2 : 'Adoração',
          type3 : null
        }
      ]
    };
  },
  methods : {
    musicModalShow  (index) {
      console.log(this.musics[index]);
    },
    getMusics (page) {
      let musicsShow = []
      for (let i = 0; i < 5; i++) {
        musicsShow.push(musics[5 * (page - 1) + i])
      }
      return musicsShow
    }
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