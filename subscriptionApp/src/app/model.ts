export class subscriptionModel {
  'Provider_Name'!: string;
  'Created_On'!: string;
  'Current_Start_Date'!: string;
  'Current_End_Date'!: string;
  'Is_Automatic_Payment_Enabled'!: string;
  'Last_Modified_On'!: string;
}

export class subDetailModel {
  'Amount_Paid'!: string;
  'Started_On'!: string;
  'Ends_On'!: string;
  'Invoice_File'!: File;
  'subscription'!: Number;
}
