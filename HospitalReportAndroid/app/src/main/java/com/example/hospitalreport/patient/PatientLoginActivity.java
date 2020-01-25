package com.example.hospitalreport.patient;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.hospitalreport.R;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class PatientLoginActivity extends AppCompatActivity {

    @BindView(R.id.patient_register)
    TextView patientRegister;

    @BindView(R.id.patient_login_button)
    Button patientloginButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_patient_login);
        ButterKnife.bind(this);
    }

    @OnClick(R.id.patient_register)
    public void patientRegisterForm() {
        Intent intent = new Intent(PatientLoginActivity.this, PatientRegisterActivity.class);
        startActivity(intent);
    }

    @OnClick(R.id.patient_login_button)
    public void poatientLogin() {
        Intent intent = new Intent(PatientLoginActivity.this, PatientDetailActivity.class);
        startActivity(intent);
    }
}
