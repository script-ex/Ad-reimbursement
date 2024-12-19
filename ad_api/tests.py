from django.test import TestCase, Client
from django.urls import reverse
from .models import Ad

class AdReimbursementTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Ad Reimbursement</h1>')

    def test_ad_creation(self):
        response = self.client.post(reverse('home'), {'ad_type': '0011', 'date': '2023-10-01', 'ads_run': 5, 'spend': 1000}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Ad.objects.count(), 1)
        ad = Ad.objects.first()
        self.assertEqual(ad.ad_type, '0011')
        self.assertEqual(ad.ads_run, 5)
        self.assertEqual(ad.spend, 1000)

    def test_ad_reimbursement_calculation(self):
        ad = Ad.objects.create(ad_type='0011', date='2023-10-01', ads_run=5, spend=1000)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'<td>{ad.ad_type}</td>')
        self.assertContains(response, f'<td>{ad.date}</td>')
        self.assertContains(response, f'<td>{ad.ads_run}</td>')
        self.assertContains(response, f'<td>{ad.spend}</td>')
        self.assertContains(response, f'<td>{ad.ads_run * ad.spend}</td>')
        self.assertContains(response, f'<td>{(ad.ads_run * ad.spend) / 2}</td>')
