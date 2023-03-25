import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DomainComponent } from "./views/domain/domain.component";
import { DomainsComponent } from "./views/domains/domains.component";
import { HomeComponent } from "./views/home/home.component";

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'domains', component: DomainsComponent },
  { path: 'domains/:domain', component: DomainComponent },
  { path: '**', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
