import { HttpClient } from '@angular/common/http';
import { subscriptionModel } from '../model';
import { subDetailModel } from '../model';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class SubscriptionService {
  private PATH_NAME = window.location.pathname.split('/')[1];
  public baseUrl = 'http://localhost:8000/api/subscriptions/';

  constructor(private http: HttpClient) {}

  addSubscrription(data: subscriptionModel): Observable<any> {
    return this.http.post(this.baseUrl, data);
  }

  getAllSubscription(): Observable<any> {
    return this.http.get(this.baseUrl);
  }

  getSubscriptionById(id: string): Observable<any> {
    return this.http.get(this.baseUrl + '/' + id);
  }

  getCurrentSubsById(id: string): Observable<any> {
    return this.http.get(this.baseUrl + '/current' + id);
  }

  getinvoice(id: string): Observable<any> {
    return this.http.get(this.baseUrl + '/' + id);
  }

  deleteSubscription(id: string): Observable<any> {
    return this.http.delete(this.baseUrl + '/' + id);
  }

  updateSubscription(data: subDetailModel): Observable<any> {
    return this.http.post(this.baseUrl + data.subscription + '/renew', data);
  }
}
