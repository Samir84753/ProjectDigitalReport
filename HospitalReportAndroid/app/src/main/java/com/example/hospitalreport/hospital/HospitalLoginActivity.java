package com.example.hospitalreport.hospital;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import com.example.hospitalreport.R;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class HospitalLoginActivity extends AppCompatActivity {

    @BindView(R.id.hospital_register)
    TextView hospitalRegister;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hospital_login);

        ButterKnife.bind(this);
    }
    @OnClick(R.id.hospital_register)
    public void hospitalRegisterForm()
    {
        Intent intent=new Intent(HospitalLoginActivity.this,HospitalRegisterActivity.class);
        startActivity(intent);
    }
}
