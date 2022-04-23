import { Component, OnInit } from '@angular/core';
import { subscriptionModel } from '../model';
import { SubscriptionService } from '../services/subscription.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-membership',
  templateUrl: './membership.component.html',
  styleUrls: ['./membership.component.css'],
})
export class MembershipComponent implements OnInit {
  constructor(public subscservice: SubscriptionService, http: HttpClient) {}

  ngOnInit(): void {}

  newSubscription = new subscriptionModel();
  Provider_Name!: any;
  Created_On!: any;
  Current_Start_Date!: any;
  Current_End_Date!: any;
  Is_Automatic_Payment_Enabled!: any;
  Last_Modified_On!: any;
  Status!: any;

  save() {
    this.subscservice.addSubscrription(this.newSubscription).subscribe(
      (res) => console.log('Saved Data sucessfull'),
      (err) => console.log(err)
    );
  }

  addSubscription() {
    this.newSubscription.Provider_Name = this.Provider_Name;
    this.newSubscription.Created_On = this.Created_On;
    this.newSubscription.Current_Start_Date = 'NA';
    this.newSubscription.Current_End_Date = 'NA';
    this.newSubscription.Is_Automatic_Payment_Enabled =
      this.Is_Automatic_Payment_Enabled;
    this.newSubscription.Last_Modified_On = 'NA';
    this.save();
  }

  addProvider(event: any) {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear();
    var date = mm + '/' + dd + '/' + yyyy;
    this.Created_On = date;
    this.Provider_Name = event.target.value;
  }
  pay(event: any) {
    this.Is_Automatic_Payment_Enabled = event.target.value;
  }
  endDate(event: any) {
    this.Current_End_Date = event.target.value;
  }
  startDate(event: any) {
    this.Current_Start_Date = event.target.value;
  }
}
