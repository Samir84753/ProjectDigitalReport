package com.example.hospitalreport;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import com.example.hospitalreport.hospital.HospitalLoginActivity;
import com.example.hospitalreport.patient.PatientLoginActivity;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class MainActivity extends AppCompatActivity {

    @BindView(R.id.hospital_card)
    CardView hospital;

    @BindView(R.id.patient_card)
    CardView patient;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ButterKnife.bind(this);


    }

    @OnClick(R.id.hospital_card)
    public void openHospitalLoginRegister()
    {
        Intent intent=new Intent(MainActivity.this, HospitalLoginActivity.class);
        startActivity(intent);
    }

    @OnClick(R.id.patient_card)
    public  void  openPatientLoginRegister()
    {
        Intent intent=new Intent(MainActivity.this, PatientLoginActivity.class);
        startActivity(intent);
    }

}
