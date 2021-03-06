<template>
    <v-container>
        <h1>Logged in as: {{ String(requestUser) }}</h1>
        <v-app id="inspire">
            <v-card>
                <v-card-title>
                    Visitors
                    <v-spacer></v-spacer>
                    <v-text-field
                    v-model="search"
                    append-icon="mdi-magnify"
                    label="Search"
                    single-line
                    hide-details
                    ></v-text-field>
                </v-card-title>
                <v-data-table
                    dense
                    v-model="selected"
                    :headers="headers"
                    :items="visitors"
                    :page.sync="page"
                    :items-per-page="itemsPerPage"
                    :sort-by="['recent_access_at']"
                    :sort-desc="[false, true]"
                    :search="search"
                    :single-select="singleSelect"
                    :loading="loading"
                    item-key="id"
                    show-select
                    multi-sort
                    class="elevation-1"
                    loading-text="Loading... Please wait"
                    hide-default-footer
                    @page-count="pageCount = $event"
                >
                    <template v-slot:top>
                        <v-switch
                        v-model="singleSelect"
                        label="Single select"
                        class="pa-3"
                        ></v-switch>
                    </template>
                    <template v-slot:item.name="{ item }">
                        <v-edit-dialog
                            :return-value.sync="item.name"
                            large
                            persistent
                            @save="save(item)"
                            @cancel="cancel"
                            @open="open"
                            @close="close"
                        > {{ item.name }}
                            <template v-slot:input>
                                <v-text-field
                                    v-model="item.name"
                                    :rules="[max40chars]"
                                    label="Edit"
                                    single-line
                                    counter
                                    autofocus
                                ></v-text-field>
                            </template>
                        </v-edit-dialog>
                    </template>
                    <template v-slot:item.photo="{ item }">
                    <div class="p-2">
                        <v-img :src="item.photo" :alt="item.name" width="100px" height="100px"></v-img>
                    </div>
                    </template>
                </v-data-table>
                <div class="text-center pt-2">
                    <v-pagination
                        v-model="page"
                        :length="pageCount"
                    ></v-pagination>
                    <v-text-field
                        class="pl-12 pr-12"
                        :value="itemsPerPage"
                        label="Items per page"
                        type="number"
                        min="-1"
                        max="15"
                        @input="itemsPerPage = parseInt($event, 10)"
                    ></v-text-field>
                </div>
            </v-card>
        </v-app>
    </v-container>
</template>

<script>
import { axios } from "@/common/api.service.js";
export default {
    name: "Manager",
    data() {
        return {
            requestUser: window.localStorage.getItem("username"),
            // requestUser: null,
            visitors: [],
            next: null,
            loadingVisitors: false,
            page: 1,
            pageCount: 0,
            itemsPerPage: 10,
            singleSelected: false,
            selected: [],
            search: '',
            headers: 
            [
                { text: 'id', value: 'id', align: 'start', sortable: false },
                { text: 'name', value: 'name' },
                { text: 'photo', value: 'photo', sortable: false, filterable: false,},
                { text: 'visits_count', value: 'visits_count' },
                { text: 'recent_access_at', value: 'recent_access_at' },
                { text: 'created_at', value: 'created_at' },
                { text: 'updated_at', value: 'updated_at' },
            ],
            max40chars: v => v.length <= 40 || 'Input too long!',
        };
    },
    methods: {
        checkAuth () {
            // check if a current user is authorized
            if (this.requestUser === null) {
                alert("invalid access");
                window.location.href = process.env.VUE_APP_LOGINPAGE
                // this.$router.push({ name: "page-not-found" });
                this.$router.push(process.env.VUE_APP_LOGINPAGE);
            }
        },
        async setUserInfo() {
            // add the username of the current user to localStorage
            try {
                const response = await axios.get(process.env.VUE_APP_USERINFOURL);
                const requestUser = response.data["username"];
                window.localStorage.setItem("username", requestUser);
                console.log('requestUser(Home):', window.localStorage.getItem("username"));
            } catch (error) {
                console.log(error.response);
                console.log(this.requestUser)
                alert(error.response.statusText);
            }
        },
        
        async getToken() {
            // get a token to access REST API
            let endpont = process.env.VUE_APP_TOKENURL;
            try {
                const data = {username: process.env.VUE_APP_USERNAME, password: process.env.VUE_APP_PASSWORD};
                const response = await axios.post(endpont, data);
                const requestAuthtoken = response.data["auth_token"];
                window.localStorage.setItem("auth_token", requestAuthtoken);
                console.log('auth_token', window.localStorage.getItem("auth_token"));
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
        },
        async getVisitors() {
            // make a GET Request to the visitors list endpoint and populate the visitors array
            await new Promise(r => setTimeout(r, 500));
            const headers = {"Authorization": `Token ${window.localStorage.getItem("auth_token")}`}
            let endpoint = process.env.VUE_APP_VISITORSURL;
            if (this.next) { // for future purpose
                endpoint = this.next;
            }
            this.loadingVisitors = true; // for future purpose
            // get all the visitors with REST API
            try {
                const response = await axios.get(endpoint, {headers});
                this.visitors.push(...response.data);
                console.log('visitors', this.visitors);
                this.loadingVisitors = false;
                if (response.data.next) {
                    this.next = response.data.next
                } else {
                    this.next = null;
                }
            } catch (error) {
                console.log(error.response);
                alert(error.response);
            }
        },
        save (item) {
            const headers = {"Authorization": `Token ${window.localStorage.getItem("auth_token")}`};
            let endpoint = `${process.env.VUE_APP_VISITORSURL}${item.id}/`;
            const data = {
                name: item.name,
            }
            try {
                axios.patch(endpoint, data, {headers});
            } catch (error) {
                console.log(error.response)
                alert(error.response)
            }
        },
    },
    created() {
        document.title = "Manager";
        this.setUserInfo();
        this.checkAuth();
        this.getToken();
        this.getVisitors();
    },
}
</script>

<style scoped>
div {
  text-align: center;
}
table, th, td {
  border: 1px solid black;
}
</style>