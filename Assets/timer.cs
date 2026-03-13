using UnityEngine;

public class timer : MonoBehaviour
{
    //The timer starts at zero
    public float Timer = 0;

    void Start() { }


    void Update()
    {
        //The timer is always counting down
        //Most of the time it'll be under zero
        Timer -= Time.deltaTime;
        //If the timer is under zero, you can move
        //If it's over zero, you can't move
        if (Timer <= 0)
        {
            //Put all your movement code here
        }

    }




    private void OnCollisionEnter2D(Collision2D other)
    {
        //When you bump into a coin, set the timer to 3
        //For three seconds, the Timer variable will be over 0
        //You won't be able to move until it reaches 0 again
        Timer = 3;
    }
}
