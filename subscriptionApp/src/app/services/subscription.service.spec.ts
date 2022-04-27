import { TestBed, inject } from '@angular/core/testing';
import {
  HttpClientTestingModule,
  HttpTestingController,
} from '@angular/common/http/testing';
import { SubscriptionService } from './subscription.service';
import { subscriptionModel } from '../model';

describe('SubscriptionService', () => {
  let service: SubscriptionService;
  let httpTestingController: HttpTestingController;
  let baseUrl = '';
  let subscribtion: subscriptionModel;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
    });
    service = TestBed.inject(SubscriptionService);
    subscribtion = {
      Provider_Name: 'Netflix',
      Created_On: '20/03/2022',
      Current_Start_Date: '22/04/2022',
      Current_End_Date: '1/5/2022',
      Is_Automatic_Payment_Enabled: true,
      Last_Modified_On: '',
    };
  });

  it('subscription added', () => {
    service.addSubscrription(subscribtion).subscribe((res: any) => {
      expect(res).toEqual(subscribtion);
    });
  });

  it('should return all subscription', () => {
    let result: subscriptionModel[] = [];
    service.getAllSubscription().subscribe((r: any) => {
      result = r;
      expect(r.length).toBe(1);
      expect(result[0]).toEqual(subscribtion);
    });
    const req = httpTestingController.expectOne(service.baseUrl);
    expect(req.request.method).toBe('GET');
    req.flush([subscribtion]);
  });

  it('should get one subscription by ID', () => {
    service.getSubscriptionById('1').subscribe((res) => {
      expect(res).toEqual(subscribtion);
    });

    const req = httpTestingController.expectOne(service.baseUrl + '/' + 1);
    expect(req.request.method).toBe('GET');
    req.flush(subscribtion);
  });

  it('should delete one subscription', () => {
    service.deleteSubscription('1').subscribe((res) => {
      expect(res).toEqual(subscribtion);
    });

    const req = httpTestingController.expectOne(service.baseUrl + '/' + '1');
    expect(req.request.method).toBe('DELETE');
    req.flush(subscribtion);
  });
});
