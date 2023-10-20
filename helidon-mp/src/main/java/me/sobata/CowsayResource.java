
package me.sobata;

import com.github.ricksbrown.cowsay.Cowsay;
import jakarta.enterprise.context.RequestScoped;
import jakarta.inject.Inject;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.QueryParam;
import java.util.*;
import java.util.logging.Logger;
import org.eclipse.microprofile.config.inject.ConfigProperty;

@Path("/cowsay")
@RequestScoped
public class CowsayResource {


    @GET
    @Path("/say")
    public String say(@QueryParam("say") Optional<String> message, @QueryParam("cowfile") Optional<String> cowfile) {
        var env = message.map(m -> System.getenv(m));
        var params = new String[] { "-f", "default", "Hello" };
        return Cowsay.say(params);
    }

}



