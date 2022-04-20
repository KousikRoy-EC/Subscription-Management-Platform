import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MembershipComponent } from './membership/membership.component';
import { RenewMembershipComponent } from './renew-membership/renew-membership.component';

const routes: Routes = [
  {
    path: 'subscribe',
    component: MembershipComponent,
  },
  {
    path: 'renew',
    component: RenewMembershipComponent,
  },
  {
    path: '*',
    redirectTo: 'subscribe',
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
