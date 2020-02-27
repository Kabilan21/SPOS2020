#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
    int n=4;
    int bt[n],wt[n],tat[n],i,avgtat=0,avgwt=0;
    for(i=0;i<n;i++)
    {
        cin>>bt[i];
    }
    wt[0]=0;
    for(i=1;i<n;i++)
    {
        wt[i]=bt[i-1]+ wt[i-1];

    }
    for(i=0;i<n;i++)
    {
        tat[i]=wt[i]+bt[i];
        avgtat+=tat[i];
        avgwt+=wt[i];
    }
    cout<<"Process\tburst time\tWaititng_time\tturn around_time\n";

    for(i=0;i<n;i++)
    {
        cout<<i<<'\t'<<bt[i]<<'\t'<<wt[i]<<'\t'<<tat[i]<<'\n';

    }
    cout<<"the average waititng time and turn around time are:"<<avgwt/4<<" "<<avgtat/4;
}
