import { Component, OnInit } from '@angular/core';
import { Childmodel } from '../model';
import { SubscriptionService } from '../services/subscription.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-renew-membership',
  templateUrl: './renew-membership.component.html',
  styleUrls: ['./renew-membership.component.css'],
})
export class RenewMembershipComponent implements OnInit {
  constructor(public subscservice: SubscriptionService, http: HttpClient) {}

  ngOnInit(): void {}

  upgradeModel = new Childmodel();
  Amount_Paid!: any;
  Started_On!: any;
  Ends_On!: any;
  Invoice_File!: any;

  save() {
    this.subscservice.updateSubscription(this.upgradeModel).subscribe(
      (res) => console.log('Saved Data sucessfull'),
      (err) => console.log(err)
    );
  }

  update() {
    this.upgradeModel.Amount_Paid = this.Amount_Paid;
    this.upgradeModel.Ends_On = this.Ends_On;
    this.upgradeModel.Started_On = this.Started_On;
    this.upgradeModel.Invoice_File = this.Invoice_File;
    this.save();
  }

  amountPaid(event: any) {
    this.Amount_Paid = event.target.value;
  }

  startOn(event: any) {
    this.Started_On = event.target.value;
  }

  endOn(event: any) {
    this.Ends_On = event.target.value;
  }

  invoice(event: any) {
    this.Invoice_File = event.target.files[0];
  }
}
