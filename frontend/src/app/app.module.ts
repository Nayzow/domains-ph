import {NgModule} from '@angular/core';
import {AppComponent} from './app.component';
import {RouterOutlet} from '@angular/router';
import {AppRoutingModule} from "./app.routing.module";
import {HttpClientModule} from "@angular/common/http";
import {NavbarComponent} from "./components/navbar/navbar.component";
import {FooterComponent} from "./components/footer/footer.component";
import {DomainComponent} from "./views/domain/domain.component";
import {DomainsComponent} from "./views/domains/domains.component";
import {MapComponent} from "./components/map/map.component";
import {SearchbarComponent} from "./components/searchbar/searchbar.component";
import {HomeComponent} from "./views/home/home.component";
import {BrowserModule} from '@angular/platform-browser';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavbarComponent,
    FooterComponent,
    SearchbarComponent,
    DomainComponent,
    DomainsComponent,
    MapComponent,
    // LoadingComponent,
  ],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        HttpClientModule,
        RouterOutlet,
        AppRoutingModule,
        FormsModule,
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
