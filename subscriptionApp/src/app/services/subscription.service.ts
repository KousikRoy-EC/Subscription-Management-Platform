import { HttpClient } from '@angular/common/http';
import { Mymodel } from '../model';
import { Childmodel } from '../model';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class SubscriptionService {
  private PATH_NAME = window.location.pathname.split('/')[1];
  public baseUrl = 'http://localhost:8000/api/subscriptions/';

  constructor(private http: HttpClient) {}

  addSubscrription(data: Mymodel): Observable<any> {
    return this.http.post(this.baseUrl, data);
  }

  getAllSubscription(): Observable<any> {
    return this.http.get(this.baseUrl);
  }

  getSubscriptionById(id: string): Observable<any> {
    return this.http.get(this.baseUrl + '/' + id);
  }

  getinvoice(id: string): Observable<any> {
    return this.http.get(this.baseUrl + '/' + id);
  }

  updateSubscription(data: Childmodel): Observable<any> {
    return this.http.post(this.baseUrl + 'update' + '/', data);
  }
}
