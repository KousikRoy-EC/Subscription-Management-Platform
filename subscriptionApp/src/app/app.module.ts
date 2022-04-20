import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MembershipComponent } from './membership/membership.component';
import { RenewMembershipComponent } from './renew-membership/renew-membership.component';

@NgModule({
  declarations: [
    AppComponent,
    MembershipComponent,
    RenewMembershipComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
