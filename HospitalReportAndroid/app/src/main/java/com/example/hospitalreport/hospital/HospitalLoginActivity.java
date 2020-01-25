package com.example.hospitalreport.hospital;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.hospitalreport.R;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class HospitalLoginActivity extends AppCompatActivity {

    @BindView(R.id.hospital_register)
    TextView hospitalRegister;

    @BindView(R.id.hospital_login_button)
    Button hospitalLoginButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hospital_login);

        ButterKnife.bind(this);
    }

    @OnClick(R.id.hospital_register)
    public void hospitalRegisterForm() {
        Intent intent = new Intent(HospitalLoginActivity.this, HospitalRegisterActivity.class);
        startActivity(intent);
    }

    @OnClick(R.id.hospital_login_button)
    public void hospitalLogin() {
        Intent intent=new Intent(HospitalLoginActivity.this,HospitalsDetailActivity.class);
        startActivity(intent);

    }
}
